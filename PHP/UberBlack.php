<?php
require_once('car,php');
class UberBlack extends Car{
    public $typeCarAccepted;
    public $seatsMaterial;


    public function __construct($license, $driver, $brand, $model,$typeCarAccepted,$seatsMaterial){
        parent::__construct($license,$driver)
        $this->typeCarAccepted= $typeCarAccepted;
        $this->seatsMaterial = $seatsMaterial;
    }


}



?>