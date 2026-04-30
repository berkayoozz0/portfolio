/*
 * adc.h
 *
 *  Created on: Jul 31, 2025
 *      Author: unknown
 */

#include <stdint.h>

#ifndef ADC_H_
#define ADC_H_
void pa1_adc_init(void);
uint32_t adc_read(void);
void conv_start(void);

#endif /* ADC_H_ */
