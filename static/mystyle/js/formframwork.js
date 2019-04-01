/**
 * Created by 病名爲愛 on 2019/3/31.
 */

$(document).ready(function(){
//    项目添加JS校验
    $("#project_post").click(function(){
        var $formData = new FormData();
        $formData.append("project_name", $("#project_name").val());
        $formData.append("project_desc", $("#project_desc").val());
        $.ajax({
            url: '/project_ajax/',
            type: "POST",
            data: $formData,
            contentType: false,
            processData: false,
            dataType: "json",
            headers: {"X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val()},
            success: function(data){
                return data
            }

        });
    });
});
