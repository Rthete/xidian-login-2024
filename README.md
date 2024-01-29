<!--
 * @FilePath: \xidian-login\README.md
 * @Description:  
 * @Author: rthete
 * @Date: 2024-01-28 22:13:45
 * @LastEditTime: 2024-01-28 22:20:35
-->
# xidian-login-2024

针对西电校园网的自动登录脚本，以解决假期实验室断电恢复后设备无法自行联网的问题。

使用selenium库和chrome驱动模拟登陆行为，脚本通过向baidu发送请求检测网络连通性，连接失败将每隔120秒重试。

## How-to-use

1. 设置校园网账号密码；

2. 安装chrome驱动，并配置驱动位置；

3. pyinstaller打包为可执行程序；

4. 设置自动启动。

   - bios设置断电重启；

   - Windows10设置任务计划程序。

**注意关闭代理*

## Reference

[校园网自动登录脚本](https://blog.csdn.net/sdfghjklg/article/details/127328595)

[设置开机自动运行](https://zhuanlan.zhihu.com/p/370801224?ivk_sa=1024320u&utm_id=0)

[通过get接口模拟登录：认证协议分析](https://blog.csdn.net/qq_41797946/article/details/89417722)