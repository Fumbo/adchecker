$(document).ready(function () {
    $('#campagnes').DataTable({
        "sDom": "<'row'<'col-sm-6'l><'col-sm-6'f>r>t<'row'<'col-sm-6'i><'col-sm-6'p>>",
        pagingType: "simple_numbers"
    });
});