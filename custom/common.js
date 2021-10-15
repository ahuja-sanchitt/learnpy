var Getproductsurl= 'http://127.0.0.1:5000/getproducts';
var addproducturl= 'http://127.0.0.1:5000/insertProducts';
var deleteproducturl='http://127.0.0.1:5000/deleteProduct';
var getunitsurl='http://127.0.0.1:5000/getunits';
var ordersaveurl='http://127.0.0.1:5000/insertOrder';
var getallorders='http://127.0.0.1:5000/getallorders';
function callApi(method,url,data){
    $.ajax({
        method:method,
         url:url ,
         data: data 
        }).done(function(msg){
            window.location.reload(); 
        });
    
}

function calculateValue(){
    var total=0;
    $(".product-item").each(function(index) {

        var qty=parseFloat($(this).find('.product-qty').val());
        var price=parseFloat($(this).find('#product_price').val());
        price=price*qty;
        $(this).find('#item_total').val(price.toFixed(2));
        total+=price;

    });

    $("#product_grand_total").val(total.toFixed(2))

}



function productParser(product) {
    return {
        id : product.id,
        name : product.employee_name,
        unit : product.employee_name,
        price : product.employee_name
    }
}


