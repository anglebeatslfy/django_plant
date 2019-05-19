function is_file() {
    var objfile = document.getElementById("upfile");
        if(objfile.value == ""){
            alert("上传文件不能为空！");
            return false;
        }
        return true;
}
function viewmypic(mypic,upfile) {
    if(upfile.files && upfile.files[0])
    {
    mypic.style.display="";
    //火狐下，直接设img属性
    //mypic.src = upfile.files[0].getAsDataURL();

     //火狐7以上版本不能用上面的getAsDataURL()方式获取，需要一下方式
    mypic.src = window.URL.createObjectURL(upfile.files[0]);
    }
    else
    {
    //IE下
    if (upfile.value){
    mypic.src=upfile.value;
    mypic.style.display="";
    mypic.border=1;
    }
    }
    }