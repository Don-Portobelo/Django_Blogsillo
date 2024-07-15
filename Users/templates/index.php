<?php
require __DIR__.'/vendor/autp;pad.php';
MercadoPago\SDK::setAccessToken('TOKEN');
$preference = new MercadoPago\Preference();
$preference->back_urls=array("succes"=>"Login.html", "failure"=>"Registro_Usuario.html", "pending"=>"Ingresar_Categoria.html");

$item = new MercadoPago\Item();
$item->is = 1;
$item->tittle = "Libro1";
$item->description = "LunadePluton";
$item->quantity = 1;
$item->unit_price = 10000;
$item->currency_id = 'CLP';
$item->items = array($item);
$item->save();
$preference->items = array($item);
$preference->save();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MercadoPago</title>
</head>
<script src="https://sdk.mercadopago.com/js/v2"></script>
<body>
    <script>
        const mp = new MercadoPago('Public Key',{
            locale: 'es-CHL'
        });
        const checkout = mp.checkout({
            preference: {
                id: '<?php echo $preference->id;?>'
            },
            render: {
                container: '.btnPagar',
                label: 'Pagar',
            }
        })
    </script>
    <a href="<?php echo $preference-init_point;?>">pagar</a>
</body>
</html>