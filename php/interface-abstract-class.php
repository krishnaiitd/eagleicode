<?php

interface Iterface1 
{
	public function GetValue() ;
	public function SetValue($value);
}

abstract class AbstractClass1 implements Iterface1 
{
	public $value;

	abstract public function GetValue();

	public function SetValue($value) {
		if (empty($value)) {
			echo 'set value is empty';
			return;
		}

		$this->value = $value;
		
	}
}

class Test extends AbstractClass1 
{
	public function GetValue() {
		return $this->value;
	}
}



$t = new Test();

$t->SetValue('krishna');

echo $t->GetValue();

echo "\n";

?>


	df <- data.frame(a = c(1,5,7,9))

	if (sum(df$a < 10) == nrow(df)) {
	b = data.frame(1:10)
	} else if (sum(df$a < 14) == nrow(df)) {
	b = data.frame(11:14)
	} else if (sum(df$a < 29) == nrow(df)) {
	b = data.frame(15:29)
	}



	> b
	   X1.10
	1      1
	2      2
	3      3
	4      4
	5      5
	6      6
	7      7
	8      8
	9      9
	10    10