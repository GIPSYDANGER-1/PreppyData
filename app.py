import os
import pandas as pd
import numpy as np
from flask import Flask, request, render_template, send_file
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

app = Flask(__name__)

def handle_missing_values(df, method):
    """결측치 처리 함수"""
    if method == 'mean':
        return df.fillna(df.mean())
    elif method == 'median':
        return df.fillna(df.median())
    elif method == 'drop':
        return df.dropna()
    return df

def handle_outliers(df, method):
    """이상치 처리 함수"""
    if method == 'iqr':
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]
    
    elif method == 'zscore':
        z_scores = np.abs((df - df.mean()) / df.std())
        return df[(z_scores < 3).all(axis=1)]
    
    return df

def scale_data(df, method):
    """스케일링 함수"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    scaler = None
    
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    elif method == 'robust':
        scaler = RobustScaler()
    
    if scaler is not None:
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df

def encode_categorical(df, method):
    """인코딩 함수"""
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    if method == 'onehot':
        df = pd.get_dummies(df, columns=categorical_cols)
    elif method == 'label':
        le = LabelEncoder()
        for col in categorical_cols:
            df[col] = le.fit_transform(df[col].astype(str))
    
    return df

@app.route('/')
def home():
    return render_template('home.html')  # 메인 페이지

@app.route('/index')
def index_page():
    return render_template('index.html')  # 추가 페이지

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/process', methods=['POST'])
def process_data():
    """데이터 전처리 라우트"""
    if 'file' not in request.files:
        return "파일이 업로드되지 않았습니다.", 400
    
    file = request.files['file']
    
    # 파일 형식 확인
    if file.filename == '':
        return "유효하지 않은 파일입니다.", 400
    
    # 파일 읽기
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.filename.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file)
    else:
        return "지원되지 않는 파일 형식입니다.", 400
    
    # 요청된 전처리 옵션 가져오기
    missing_method = request.form.get('missing', 'mean')
    outlier_method = request.form.get('outlier', None)
    scaling_method = request.form.get('scaling', None)
    encoding_method = request.form.get('encoding', None)
    
    # 전처리 수행
    df = handle_missing_values(df, missing_method)
    
    if outlier_method:
        df = handle_outliers(df, outlier_method)
    
    if scaling_method:
        df = scale_data(df, scaling_method)
    
    if encoding_method:
        df = encode_categorical(df, encoding_method)
    
    # 결과 저장
    output_path = 'preprocessed_data.csv'
    df.to_csv(output_path, index=False)
    
    # 파일 다운로드
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)