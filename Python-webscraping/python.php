<?php
    $command = escapeshellcmd('./product_detail_scrap-1.py');
    $url = "https://www.doordash.com/store/taco-bell-ogdensburg-23109443/?pickup=false"
    $output = shell_exec( python3 $command $url);
    echo $output;
?>