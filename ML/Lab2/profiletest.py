from pandas_profiling import ProfileReport

my_data =  'C:/Users/lehak/Videos/ML/Lab2/attacks.csv' 
profile = ProfileReport(my_data, title="Pandas Profiling Report")

# запускаем показ профиля
profile.to_file("my_report.html")