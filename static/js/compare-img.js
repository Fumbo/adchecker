function GoTest(current) {
    resemble('/static/images/loading-mini.gif').compareTo('/static/images/loading-mini.gif').ignoreColors().onComplete(function(data){
        console.log(data);
        id = current.attr('id');
        if(data.misMatchPercentage == 0){
            $('#loading-'+id).hide();
            $('#test'+id+'-good').show();
            $('#'+id).addClass('success')
        }
        /*
           {
           misMatchPercentage : 100, // %
           isSameDimensions: true, // or false
           dimensionDifference: { width: 0, height: -1 }, // defined if dimensions are not the same
           getImageDataUrl: function(){}
           }
           */
    });
};

$(".test").click(function() {
    GoTest($(this));
});
