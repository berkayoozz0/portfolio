#include "stm32f4xx.h"

#define SYST_LOAD_VAL	16000
#define SYST_EN			(1U<<0)
#define COUNTFLAG		(1U<<16)
#define CLK_SRC			(1U<<2)


void sysTickDelayMs(int ms)
{
	/*Reload with number of clocks per miliseconds*/
	SysTick->LOAD = SYST_LOAD_VAL;
	/*Clear SysTick current value register*/
	SysTick->VAL = 0;
	/*Enable SysTick and select internal clk src*/
	SysTick->CTRL |= SYST_EN;
	SysTick->CTRL |= CLK_SRC;

	/*Loop*/
	for(int i=0; i<ms ; i++){
		/*Wait until the countflag is set.*/
		while((SysTick->CTRL & COUNTFLAG) == 0){
		}
	}
}
