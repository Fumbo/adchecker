$(document).ready(function () {
    var campagnes_table = $('#campagnes');
    campagnes_table.DataTable({
        "sDom": "<'row'<'col-sm-6'l><'col-sm-6'f>r>t<'row'<'col-sm-6'i><'col-sm-6'p>>",
        pagingType: "simple_numbers",
        "columnDefs": [
            { "type": "title-string", targets: 5}
        ]
    });
    campagnes_table.on('click', 'a.image', function () {
        $('#img-dest').attr('src', $(this).data('src'));
    });
});