$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-brew .modal-content").html("");
        $("#modal-brew").modal("show");
      },
      success: function (data) {
        $("#modal-brew .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#brew-table tbody").html(data.html_brew_list);
          $("#modal-brew").modal("hide");
        }
        else {
          $("#modal-brew .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create brew
  $(".js-create-brew").click(loadForm);
  $("#modal-brew").on("submit", ".js-brew-create-form", saveForm);

  // Update brew
  $("#brew-table").on("click", ".js-update-brew", loadForm);
  $("#modal-brew").on("submit", ".js-brew-update-form", saveForm);

  // Delete brew
  $("#brew-table").on("click", ".js-delete-brew", loadForm);
  $("#modal-brew").on("submit", ".js-brew-delete-form", saveForm);

});