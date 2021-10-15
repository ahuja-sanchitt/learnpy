var productModal = $("#productModal");
    $(function () {

        //JSON data by API call
        $.get(Getproductsurl, function (response) {
            if(response) {
                var table = '';
                $.each(response, function(index,product) {
                    table += '<tr data-id="'+ product.p_id +'" data-name="'+ product.P_name +'" data-unit="'+ product.unit_id +'" data-price="'+ product.price +'">' +
                        '<td>'+ product.P_name +'</td>'+
                        '<td>'+ product.unit_id+'</td>'+
                        '<td>'+ product.price +'</td>'+
                        '<td><span class="delete-product">Delete</span></td></tr>';
                });
                $("table").find('tbody').empty().html(table);
            }
        });
    });

    $(document).on("click",".delete-product",function(){
        var tr=$(this.closest('tr'));
        var data= { p_id : tr.data('id')};
        var isDelete=confirm("are you sure to delete "+tr.data('name')+" item?");
        if(isDelete) {
            callApi("POST", deleteproducturl,data);
        }
    });

     // Save Product
     $("#saveProduct").on("click", function () {
        // If we found id value in form then update product detail
        var data = $("#productForm").serializeArray();
        var requestPayload = {
            name: null,
            unit_id: null,
            price: null
        };
        for (var i=0;i<data.length;++i) {
            var element = data[i];
            switch(element.name) {
                case 'name':
                    requestPayload.name = element.value;
                    break;
                case 'uoms':
                    requestPayload.Unit_id = element.value;
                    break;
                case 'price':
                    requestPayload.price = element.value;
                    break;
            }
        }
        alert('Product has been added!')
        callApi("POST", addproducturl, {
            'data': JSON.stringify(requestPayload)
        });
    });

    


    productModal.on('hide.bs.modal', function(){
        $("#id").val('0');
        $("#name, #unit, #price").val('');
        productModal.find('.modal-title').text('Add New Product');
    });

    

       

    productModal.on('show.bs.modal', function(){

        //JSON data by API call
        $.get( getunitsurl, function (response) {
            if(response) {
                var options = '<option value="">--Select--</option>';
                $.each(response, function(index, uom) {
                    options += '<option value="'+ uom.unit_id +'">'+ uom.unit_name +'</option>';
                });
                $("#uoms").empty().html(options);
            }
        });
    });
    