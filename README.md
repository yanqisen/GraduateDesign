# GraduateDesign
**My GraduateDesign of Bachelor**  
data里存放训练集，以及测试集。  
首先创建file文件，然后运行word.py进行预处理，utils里是url解码的工具，testurldecode用来测试utils。  
运行cnn.py对数据进行训练，得到检测模型。  
或者使用mlp.py来训练，同样的到检测模型。
然后运行test_normal.py来测试模型。 
网站后台使用django。  
将file文件夹和test.py以及模型copy进sql_detect文件夹，然后用python manage.py runserver运行服务器，进行简单测试，目前仅支持单行数据，后续加入多行测试。 
测试数据使用HTTP协议内容，可以自己抓包和获取别的含有攻击的包。  