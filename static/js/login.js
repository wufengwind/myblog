/* @File  : login.js
 * @Author: 吴丰
 * @Date  : 2019.08.23
 **@Software: PyCharm*/
function sub() {
    var login=document.getElementById("for");
    var password_f=document.getElementById("re_pass").value;
    var password_s=document.getElementById("re_pass2").value;
    if(password_f===password_s) {
        login.submit();
    }
    else{
        alert('两次输入密码不一致');
        return false;
    }
}
