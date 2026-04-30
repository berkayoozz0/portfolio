#include <stdio.h>
#include <stdint.h>
#include "stm32f4xx.h"
#include "uart.h"
#include "adc.h"
#include "systick.h"
#include "tim.h"
#include "exti.h"


#define GPIOAEN			(1U<<0)
#define PIN5			(1U<<5)
#define LED_PIN			PIN5


int main(void)
{

	uart2_rxtx_init();
	RCC->AHB1ENR |=  GPIOAEN;
	GPIOA->MODER |=  (1U<<10);
	GPIOA->MODER &=~ (1U<<11);
	pc13_exti_init();
	while(1)
{
}
}

static void exti_callback(void)
	{
		printf("BTN pressed...\n\r");
		GPIOA->ODR^=LED_PIN;
	}

void EXTI15_10_IRQHandler(void) {
	if((EXTI->PR & LINE_13)!=0)
	{
		/*Clear PR flag*/
		EXTI->PR |= LINE_13;
		/*Do something*/
		exti_callback();
	}
}
