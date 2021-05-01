<?php
$username = $argv[1];
$apikey = $argv[2];
$id = $argv[3];
require('MulticraftAPI.php');
$api = new MulticraftAPI('https://mc.pebblehost.com/api.php', $username, $apikey);
print_r($api->getServer($id));
?>