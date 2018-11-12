
function getXhr(){
    //如果浏览器支持XMLHttpRequest，则创建XMLHttpRequest对象并返回
    if(window.XMLHttpRequest){
        return new XMLHttpRequest();
    }
    else{
        //如果不支持XMLHttpRequest的话，则创建ActiveXObject对象
        var xhr=new ActiveXObject('Microsoft XMLHTTP')
    }
}
