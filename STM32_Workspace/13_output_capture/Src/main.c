#include <stdio.h>
#include <stdint.h>
#include "stm32f4xx.h"
#include "uart.h"
#include "adc.h"
#include "systick.h"
#include "tim.h"


int main(void)
{

	tim2_pa5_output_compare();
	tim3_pa6_input_compare();

	while(1){

		while(!(TIM2->SR & SR_UIF)){}
		TIM2->SR &=~ SR_UIF;


		printf("A second passed!\n");
		GPIOA->ODR ^= LED_PIN;

		}


}
