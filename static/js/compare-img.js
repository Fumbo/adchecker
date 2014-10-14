$( "#loading" ).click(function() {
    resemble('/static/images/loading-mini.gif').compareTo('/static/images/loading-mini.gif').ignoreColors().onComplete(function(data){
        console.log(data);
        if(data.misMatchPercentage == 0){
            $('#test1-good').show();
            $('#test1').addClass('success')
            $('#loading').hide();
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
});
