<?php
class Base {
    public function sayHello() {
        echo 'Hello ';
    }
}

trait SayWorld {
    public function sayHello() {
        parent::sayHello();
        echo 'World!';
    }
}

class Check {
	public function checkingit()
	{
		echo 'In the chekcingit mehtod of check class, ' . get_called_class . '\n'; 
	}
}

class MyHelloWorld extends Base {
    use SayWorld;
    use Check;
}

$o = new MyHelloWorld();
$o->sayHello();
echo '\n';
$o->checkingit()

?>


