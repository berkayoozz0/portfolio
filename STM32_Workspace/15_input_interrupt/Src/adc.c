#include "stm32f4xx.h"
#include "adc.h"

#define ADC1_EN			(1U<<8)
#define GPIOA_EN		(1U<<0)
#define ADC_CH1			(1U<<0)  //0b 0000... 0001
#define ADC_SEQ_LEN_1	(0x00)
#define CR2_ADON		(1U<<0)
#define CR2_SWSTART		(1U<<30)
#define SR_EOC			(1U<<1)

void pa1_adc_init(void)
{
	/*****Configure the ADC GPIO pin*****/

	/*Enable clock access*/
	RCC->AHB1ENR |= GPIOA_EN;
	/*Set the mode of PA1 to analog*/
	GPIOA->MODER |= (1U<<2);
	GPIOA->MODER |= (1U<<3);

	/*****Configure the ADC module*****/
	/*Enable clock access*/
	RCC->APB2ENR |= ADC1_EN;
	/*Conversion sequence start*/
	ADC1->SQR3 =	ADC_CH1;
	/*Conversion sequence length*/
	ADC1->SQR1 =	ADC_SEQ_LEN_1;
	/*Enable ADC module*/
	ADC1->CR2 |= CR2_ADON;
}

void conv_start(void)
{
	/*Start the ADC conversion*/
	ADC1->CR2 |= CR2_SWSTART;
}

uint32_t adc_read(void)
{
	/*Wait for the conversion to be complete*/
	while(!(ADC1->SR & SR_EOC)){}
	/*Read converted result*/
	return (ADC1->DR);
}
