$(document).ready(function() {
    $("#cargar-historial").click(function() {
        $.ajax({
            url: "https://www.googleapis.com/books/v1/volumes?q=category:all",
            dataType: "json",
            success: function(data) {
                // Eliminar registros antiguos
                $("table tbody tr").remove();
                
                var items = [];
                $.each(data.items, function(index, value) {
                    if ($.inArray(value.volumeInfo.title, items) == -1) {
                        items.push(value.volumeInfo.title);
                        var newRow =
                            "<tr><td>" +
                            value.volumeInfo.title +
                            "</td><td>" +
                            value.volumeInfo.categories +
                            "</td><td>" +
                            value.volumeInfo.authors +
                            "</td><td>" +
                            value.volumeInfo.publishedDate +
                            "</td></tr>";
                        $("table tbody").append(newRow);
                    }
                });
            }
        });
    });
})