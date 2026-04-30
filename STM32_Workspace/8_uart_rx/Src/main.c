#include <stdio.h>
#include <stdint.h>
#include "stm32f4xx.h"
#include "uart.h"



#define GPIOAEN		(1U<<0)
#define GPIOA_5		(1U<<5)

#define PIN5		(1U<<5)
#define LED_PIN 	PIN5


char key;

int main(void)
{
	/*Enable the clock acces to GPIOA*/
	RCC->AHB1ENR |= GPIOAEN;
	/*Set PIN5 to output mode.*/
	GPIOA->MODER |= (1U<<10);
	GPIOA->MODER &= ~(1U<<11);

	uart2_rxtx_init();
	while(1)
	{
		key = uart2_read();
		if(key=='1'){
			GPIOA->ODR |=  LED_PIN;
		}
		else{
			GPIOA->ODR &= ~LED_PIN;
		}
		}
	}
