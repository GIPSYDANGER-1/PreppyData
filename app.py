from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, LabelEncoder
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_data():
    if 'file' not in request.files:
        return '파일이 업로드되지 않았습니다.', 400
    
    file = request.files['file']
    if file.filename == '':
        return '파일이 선택되지 않았습니다.', 400

    # 파일 읽기
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        return '지원하지 않는 파일 형식입니다.', 400

    # 결측치 처리
    if 'missing_mean' in request.form:
        df = df.fillna(df.mean())
    elif 'missing_median' in request.form:
        df = df.fillna(df.median())
    elif 'missing_drop' in request.form:
        df = df.dropna()

    # 이상치 처리
    if 'outlier_iqr' in request.form:
        for column in df.select_dtypes(include=[np.number]).columns:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            df = df[~((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))]
    
    elif 'outlier_zscore' in request.form:
        for column in df.select_dtypes(include=[np.number]).columns:
            z_scores = abs((df[column] - df[column].mean()) / df[column].std())
            df = df[z_scores < 3]

    # 스케일링
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    if 'scaling' in request.form:
        if request.form['scaling'] == 'standard':
            scaler = StandardScaler()
        elif request.form['scaling'] == 'minmax':
            scaler = MinMaxScaler()
        elif request.form['scaling'] == 'robust':
            scaler = RobustScaler()
        
        df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    # 인코딩
    categorical_columns = df.select_dtypes(include=['object']).columns
    if 'encoding' in request.form:
        if request.form['encoding'] == 'onehot':
            df = pd.get_dummies(df, columns=categorical_columns)
        elif request.form['encoding'] == 'label':
            le = LabelEncoder()
            for col in categorical_columns:
                df[col] = le.fit_transform(df[col].astype(str))

    # 처리된 데이터를 CSV 파일로 변환
    output = io.BytesIO()
    df.to_csv(output, index=False, encoding='utf-8-sig')
    output.seek(0)
    
    return send_file(
        output,
        mimetype='text/csv',
        as_attachment=True,
        download_name='processed_data.csv'
    )

if __name__ == '__main__':
    app.run(debug=True) 