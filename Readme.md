## 文件结构
```
+--finscrapy  #数据展示网站
|  |--app.py
|  |--config.py
|  |--run.py  #运行文件
|  |+--applications
|      |--__init__.py
|      |--initial.py
|      |--templates
|         |--index.html
|  |+--models
|      |--__init__.py
|      |--finscrapy.py
|  |+--static
|      |--chinese.json
|      |--jquery.dataTables.min.css
|      |--jquery.dataTables.min.js
|      |--jquery.min.js
+--ecb_scrapy  #爬虫框架
|  |--scrapy.cfg
|  |+--ecb_scrapy
|      |--__init__.py
|      |--items.py
|      |--middlewares.py
|      |--pipelines.py
|      |--settings.py
|      |+--spiders
|          |--__init__.py
|          |--ecbSpider.py #ecb爬虫运行文件
|          |--FRSpider.py  #FR爬虫运行文件
+--finscrapy.py  #定时任务运行文件
+--requirements.txt  #依赖包
```
## 环境依赖
* python3.6(windows下建议使用anaconda创建虚拟环境)
* mongodb数据库
* pip install -r requirements.txt 安装依赖包
## 项目部署
1、安装项目依赖的环境包

2、打开网站目录下的config.py，修改配置参数

3、输入命令"python run.py“启动网站服务器，地址为参数中"HOST:PORT"

4、切换到项目根目录下，输入命令"python finscrapy.py"启动定时任务
## config.py配置参数
config.py
```
HOST = 'localhost' #默认为localhost
PORT = 8006  #端口号，若被占用就换一个，一般取5000-10000范围内
DEBUG = True  #调试模式，为True时会暴露数据等，调试完成后请改为False
MONGODB_HOST = 'localhost'  #数据库地址
MONGODB_PORT = 27017   #数据库端口，以数据库的设置为准，不是随便写的，mongodb数据库默认端口为27017
DATABASE = 'finscrapy'  #数据库中的database名称
LOGPATH = './finscrapy_log' #日志目录，该项目未开启日志，错误信息等都利用print函数暴露在终端
SECRET_KEY = 'abcdefg'  #加密字符串
```
* 启动后浏览地址为HOST:PORT，以本配置为例，为localhost:8006，外网不可访问，只能本机访问
* SECRET_KEY参数为flask框架设定的，不填有时候会报错，保密需求高可使用os.radom函数取随机值