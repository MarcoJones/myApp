/**
 * Created by 病名爲愛 on 2019/3/31.
 */

$(document).ready(function(){
//    项目添加JS校验
    $("#project_post").click(function(){
       var p_name = $("#project_name").val();
       var p_desc = $("#project_desc").val();
        $.post('{% url "project_ajax" %}',
            {"project_name": p_name, "project_desc": p_desc},
            function(data){
               alert(data)
            }
        );

    });
});
//headers: {"X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val()},