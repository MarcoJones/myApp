/**
 * Created by 病名爲愛 on 2019/3/31.
 */

$(document).ready(function() {
    var form = $("project_form");
     form.bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            project_name: {
                message: '项目名称验证失败',
                validators: {
                    notEmpty: {
                        message: '项目名称不能为空'
                    },
                    stringLength: {
                        min: 2,
                        max: 16,
                        message: '项目名称长度必须在2-18位之间'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z0-9_]+$/,
                        message: '项目名称只能包含大小写字母、数字和下划线'
                    }
                }
            },
            project_desc: {
                message: '项目描述验证失败',
                validators: {
                    notEmpty: {
                        message: '项目描述不能为空'
                    },
                    stringLength: {
                        min: 1,
                        max: 255,
                        message: '项目描述长度必须在1-255位之间'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z0-9_]+$/,
                        message: '项目名称只能包含大小写字母、数字和下划线'
                    }
                }
            }
        }
    });
    $(form).submit(function(){
        var bv = form.data('bootstrapValidator');
        bv.validate();
        if(bv.isValid()){
            console.log(form.serialize());
            //发送ajax请求
            $.ajax({
                url: '{% url "project_ajax" %}',
                type: "POST",
                contentType: "JSON",
                data: {project_name: $("#project_name").val(), project_desc: $("#project_desc").val()},
                complete: function (msg) {
                    console.log('完成了');
                },
                success: function (result) {
                    console.log(result);
                    if(result){
                        window.location.reload();
                    }
                    else{
                        $('#returnMsg').hide().html('<label class="label label-danger">项目添加失败！</label>').show(300);
                    }
                },
                error: function(){
                    $('#returnMsg').hide().html('<label class="label label-danger">项目添加失败！</label>').show(300);
                }
            });
        }
    });
});
//    项目添加JS校验
//    $("#form_data").submit(function(){
//       var p_name = $("#project_name").val();
//       var p_desc = $("#project_desc").val();
//        //$.post('{% url "project_ajax" %}',
//        //    {"project_name": p_name, "project_desc": p_desc},
//        //    function(data){
//        //       alert(data)
//        //    }
//        //);
//        return alert('项目添加成功？')
//    });
//});
//headers: {"X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val()},