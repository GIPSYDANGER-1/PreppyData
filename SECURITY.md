# Security Policy 🔒

## Data Security Principles

### Data Processing Security 🛡️
* All data preprocessing steps are executed safely in the local environment
* Special attention is required for data containing sensitive personal information
* Data encryption and anonymization processes are recommended
* Datasets downloaded from external sources must be verified for trustworthy origins

### Secure Data Formats and Processing 📋
* Use of secure file formats is recommended for data I/O (e.g., .csv, .parquet)
* Usage of potentially dangerous formats (e.g., pickle) is restricted
* Data integrity is ensured during transformation processes
* Memory management requires attention when processing large-scale data

### Code Execution Environment Protection 💻
* Data from external sources must be validated before execution
* Execution of data processing scripts from unknown sources is prohibited
* System resource usage is monitored to prevent overload
* Virtual Environment should be used when necessary for isolated execution environments

### Data Preprocessing Safety Guidelines 📝
* Original data backups must be maintained
* Data preprocessing steps should be logged for traceability
* Sample data testing should be conducted before large-scale data transformation
* Automated preprocessing scripts must undergo code review before execution

## Version Control and Updates 🔄
* Regular security updates provided
* Immediate patches for versions with discovered vulnerabilities
* Maintenance of security issue records for previous versions
* Version updates for major data processing functionality changes

## Recommendations ✅
1. Create backups before data processing
2. Maintain latest version usage
3. Activate logging for tracking data processing steps
4. Set appropriate access permissions
5. Regular security update checks
6. Verify system requirements for large-scale data processing

## Vulnerability Reporting 📝

If you discover a security vulnerability, please report it through:

1. GitHub Security tab
2. Email: [evekha123@naver.com]

Reported vulnerabilities will be handled as follows:
* Acknowledgment within 24 hours
* Initial assessment within 72 hours
* Patch development and deployment for confirmed vulnerabilities

## External Dependency Management 🔗
* All external libraries used are regularly checked for security updates
* Library versions with discovered vulnerabilities are updated immediately
* Security review is conducted when adding new dependencies

## Supported Versions

| Version | Security Updates |
|————|————————|
| 0.0.1   | :white_check_mark:|
| < 0.0.1 | :x:             |
