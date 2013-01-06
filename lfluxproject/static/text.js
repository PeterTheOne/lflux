function initInMoreDetail(element) {
    if(element==$)
        element = document;
    element = element || document;
    element = $(element);
    var imdIDs = {};
    var createdId = 999;
    var es = element.find('.inmoredetail');
    $.each(es, function(index, value) {
            var id = $(value).attr('class').split(' ').filter(function(x) { return x.indexOf('imd-')==0; });
            if(id.length==0) {
                id = ['imd-a'+createdId];
                createdId+=1;
            }
            id = id[0];
            $(value).addClass(id);
            if(imdIDs[id]) {
                return;
            }
            var detail = value;
            var elem = null;
            if($('.label-'+id).length>0) {
                var elem = $('.label-'+id)[0];
                $(elem).addClass('manualbutton');
            } else {
                var elem = document.createElement('span');
                elem.innerHTML = '…';
                $(value).before(elem);
            }
            $(elem).addClass('imdbutton');
            $(elem).click(function() { $('.'+id).show(); $(elem).toggle(); });
            imdIDs[id] = elem;
        });
    $('.inmoredetail').click(function() {
        var id = $(this).attr('class').split(' ').filter(function(x) { return x.indexOf('imd-')==0; })
        var elem = imdIDs[id];
        $(elem).show();
        $('.'+id).hide();
    });
}
$(document).ready(initInMoreDetail);
