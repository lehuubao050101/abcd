/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2024 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "stdbool.h"
 static volatile uint16_t  c_key_num =0,d[10],num_b=0;

static volatile uint16_t stop=0,_key_ =0,_write=0,key_x =0, key_c =0,start=0,check =0,data_flash=0;
static volatile uint8_t _num =0,wait =0;
#define ROW1_PIN GPIO_PIN_12
#define ROW2_PIN GPIO_PIN_13
#define ROW3_PIN GPIO_PIN_14
#define ROW4_PIN GPIO_PIN_15
#define COL1_PIN GPIO_PIN_8
#define COL2_PIN GPIO_PIN_9
#define COL3_PIN GPIO_PIN_10
#define COL4_PIN GPIO_PIN_11
#define GPIO_KEY_ROW GPIOA
/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
char buf[16];		
void bufcl(void)
{
for(int i=0; i<16; i++)
	{
	buf[i]=' ';
	}

}


/* Private variables ---------------------------------------------------------*/
ADC_HandleTypeDef hadc1;
DMA_HandleTypeDef hdma_adc1;

I2C_HandleTypeDef hi2c1;

TIM_HandleTypeDef htim2;

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_DMA_Init(void);
static void MX_ADC1_Init(void);
static void MX_TIM2_Init(void);
static void MX_I2C1_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
uint8_t key;

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */



/* Private variables ---------------------------------------------------------*/
ADC_HandleTypeDef hadc1;
DMA_HandleTypeDef hdma_adc1;

I2C_HandleTypeDef hi2c1;

TIM_HandleTypeDef htim2;


/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_DMA_Init(void);
static void MX_ADC1_Init(void);
static void MX_TIM2_Init(void);
static void MX_I2C1_Init(void);
/* USER CODE BEGIN PFP */
 static unsigned long count =0;
/* USER CODE END PFP */
void delay_1ms(void)
{
 __HAL_TIM_SetCounter(&htim2, 0);
 while (__HAL_TIM_GetCounter(&htim2)<20);
	
}
uint32_t millis()
{
 delay_1ms();

 count ++;

return count;
}
void delay(uint16_t a){
	
for(uint16_t i =0; i<a; i++)
	{
delay_1ms();

	}

}

void timer_t(){

count =0;
}
	bool none_key(){		
if((HAL_GPIO_ReadPin(GPIO_KEY_ROW,COL1_PIN)==0)|(HAL_GPIO_ReadPin(GPIO_KEY_ROW,COL2_PIN)==0)|(HAL_GPIO_ReadPin(GPIO_KEY_ROW,COL3_PIN)==0)|(HAL_GPIO_ReadPin(GPIO_KEY_ROW,COL4_PIN)==0)){
return true;
	
}else{
return false;
	}
}
uint8_t Keypad_Read()
{
	
    // M?ng luu tr? các giá tr? c?a hàng và c?t
    
					int8_t keypad[4][4] = {
						{'1', '4', '7', 'E'},
						{'2', '5', '8', '0'},
						{'3', '6', '9', 'F'},
						{'A', 'B', 'C', 'D'},
				
					};
 
    uint16_t row_pins[4] = {ROW1_PIN, ROW2_PIN, ROW3_PIN, ROW4_PIN};

  
		
    for (uint8_t row = 0; row < 4; row++)
    {
			 HAL_GPIO_WritePin(GPIOB, ROW1_PIN| ROW2_PIN| ROW3_PIN| ROW4_PIN, GPIO_PIN_SET);
      	delay(1);
				//HAL_GPIO_WritePin(GPIOA, row_pins[row], GPIO_PIN_SET);
			HAL_GPIO_WritePin(GPIOB, row_pins[row], 0);
			
				//uint8_t check_roe = row;
				uint16_t col_pins[4] = {COL1_PIN, COL2_PIN, COL3_PIN, COL4_PIN};
				
					delay(1);
				
				
      for (uint8_t col = 0; col < 4; col++)
        {
				
          if (HAL_GPIO_ReadPin(GPIOA, col_pins[col]) == 0)
						{
					
             			
						delay(2);
						
					

						return keypad[row][col];

				
                				
				}		
				delay(1);
						
      }
				

							delay(1);
			
    } return 0x01;
}





int32_t map(int32_t value, int32_t inputMin, int32_t inputMax, int32_t outputMin, int32_t outputMax)
{
    return (value - inputMin) * (outputMax - outputMin) / (inputMax - inputMin) + outputMin;
}

float num_adc(){
	
		lcd_put_cur(1,6);
		HAL_ADC_Start(&hadc1);
		HAL_ADC_PollForConversion(&hadc1,100);
		uint16_t dat = HAL_ADC_GetValue(&hadc1);
		HAL_ADC_Stop(&hadc1);	
		HAL_Delay(50); ///-------------------------------------------------------
		bufcl();
		//float adc = map(dat,0,4095,0,5);
		float voltage = (3.3f * dat) / 4095.0f; // N?u ngu?n 5V, thay 3.3f b?ng 5.0f
		float temperature = voltage / 0.001f;
	
		lcd_put_cur(1,8);
		sprintf(buf,"T:.2%d", (uint16_t)temperature );
		lcd_send_string (buf);	
	
//	float re = (((adc * 100) / 1.88) + 0);

		return  temperature;
	
	
	
	
	
	
	
	
}





uint16_t num_key_timer(){
	int16_t _key /* = key_final()*/;
				
	if( /*(key_push()== 1)&&*/ _key != 999999)
		{
					lcd_put_cur(0,6);
				lcd_send_string ("    ");
					lcd_put_cur(0,3);
				bufcl();
				uint8_t a,b;
			if(_key<60)
					{
						a=0;
						b = _key;
					}else
					{
						b	= _key%60;
						a = (_key-b)/60;
					}	
					
					sprintf(buf,"%dp:%ds",a,b);
				lcd_send_string (buf);	
	
	}

 }

 
 
 
 
void num_write_flash(){  // GHI SO CHU KY VA NHIET DO
	
	uint8_t a=0, i=0,b=0;  		//Flash_Write_Array_16bit(uint16_t* _Array_DATA_, uint32_t _ADDRESS_DATA_, uint16_t _LENGTH_);
	uint16_t data =0,buf_data=0 ;
	
	
	//lcd_put_cur(0,4);
	//lcd_send_string ("chuky T/N");
	lcd_put_cur(0,0);
bool _ch = true;
lcd_send_string ("chuky");
	while(1)
	{
		delay(2);
	uint8_t k_ =	(uint8_t)Keypad_Read();
		
			lcd_put_cur(0,0);
		lcd_send_string ("chuky:");
		if(k_ != 0x01 && k_  < 58){ 
		data= buf_data*10 +k_ -48;
			buf_data =data;
		
		lcd_put_cur(0,0);
		bufcl();
		sprintf(buf,"chuky:%d",data );
		lcd_send_string (buf);
		}else if(k_ == 69){ // * 69
		data =0;
			buf_data=0;
			lcd_clear ();
	
			
	
		}else if(k_ == 70)  /// # 70
			{
			
			break;
			}
		
		
		
	
		
	delay(10);

	}
	data ++;
	uint32_t	flash_length = 0x08000000 +1024*123;
	 Flash_Write_Uint(data, flash_length);
	delay(100);
		data_flash = data;
		HAL_Delay(10);
		uint16_t flash_write_T[data];
		uint16_t flash_write_N[data];
		
		
	lcd_clear(); 
			lcd_put_cur(0,0);
	bufcl();
	sprintf(buf,"da chon:%d",data);
		lcd_send_string (buf);
		
		HAL_Delay(500);
	
	
		uint8_t num_nhiet=0,num_time =0;
	lcd_clear(); 
	lcd_put_cur(0,0);
	
	lcd_send_string ("ND: A");
	lcd_put_cur(0,6);
lcd_send_string ("TG: B");
	uint8_t length1 =0,length2 =0;
	uint16_t da =0,buf_da=0;
	bool check_N = false, check_T = false;
	delay(200);
		lcd_clear(); 
		
		lcd_put_cur(0,0);
		lcd_send_string ("%d-N%d");
		lcd_put_cur(0,8);
		lcd_send_string ("%d-T%d");
	do{
	delay(2);
			uint8_t k_2 =(uint8_t)	Keypad_Read();	
		if(k_2 != 0x01 && k_2<58 ){
		 da= buf_da*10 +k_2 -48;
			buf_da =da;
		}else if(k_2 == 69){
					buf_da=0;		da =0;	lcd_put_cur(1,4);	lcd_send_string ("     ");		}
		

		
			lcd_put_cur(1,4);
		bufcl();
		sprintf(buf,"%d",da);
		lcd_send_string (buf);

						// 65 A
		if( k_2 == 65 && num_nhiet==0) 		// ---------- NHAN x DE THEM NHIET DO
			{    					
					
				flash_write_N[length1] =  da;
					
				
				bufcl();
					lcd_put_cur(0,0);
				sprintf(buf,"%d-N%d ",length1,flash_write_N[length1]);
				
				lcd_send_string (buf);
				key_x =0;
			
			if(length1 >= (data))
				{
						lcd_put_cur(0,0);
					lcd_send_string ("/-/-");
				check_N = true;
					num_nhiet=1;
				}else{length1 ++;
			
				}buf_da=0;		da =0;	
		lcd_put_cur(1,4);
		lcd_send_string ("   ");
			
				
				// 66 B
		}else if(k_2 ==66 && num_time ==0) // 	// ---------- NHAN + DE THEM TH
		{										
		
		flash_write_T[length2] =  da;  		//if(length2 >= data){continue ;};
			
			
		bufcl();
		lcd_put_cur(0,8);
		sprintf(buf,"%d-T%d",length2,	flash_write_T[length2]);
		lcd_send_string (buf);	
		key_c =0;
			
			
				if(length2 >= (data))
				{
				lcd_put_cur(0,8);
				lcd_send_string ("/-/-");
			check_N = true;
				num_time=1;
				}else{length2 ++;
				
				
				}
			buf_da=0;		da =0;	
		lcd_put_cur(1,4);
		lcd_send_string ("   ");
		
	}
delay(2);

	if(k_2 == 70)
		{
lcd_clear();
			lcd_send_string ("dang luu");
		delay(20);
																	/*#define _PAGE_127_ 		 	((uint32_t)0x0801FC02)
																#define _PAGE_126_ 		 	((uint32_t)0x0801F802)
																#define _PAGE_125_ 		 	((uint32_t)0x0801F402)
																#define _PAGE_124_ 		 	((uint32_t)0x0801F002)
																#define _PAGE_123_ 		 	((uint32_t)0x0801EC02)
																#define _PAGE_122_ 		 	((uint32_t)0x0801E802)
																#define _PAGE_121_ 		 	((uint32_t)0x0801E402)
																#define _PAGE_120_ 		 	((uint32_t)0x0801E002)
																#define _PAGE_119_ 		 	((uint32_t)0x0801DC02)
																#define _PAGE_118_ 		 	((uint32_t)0x0801D802) */
		
		
			lcd_clear();
			
	for(uint8_t in=0;in<=data; in++){
			bufcl();
				lcd_put_cur(0,0);
			sprintf(buf,"%d: temp: %d",in,flash_write_N[in]);
		lcd_send_string (buf);
			bufcl();
				lcd_put_cur(1,3);
			sprintf(buf,"time: %d",flash_write_T[in]);
		lcd_send_string (buf);
 
			delay(50);
		
			}
		delay(10);
			uint32_t	ris_temp 	=	0x08000000 +1024*124;
			uint32_t	ris_timer =  0x08000000 +1024*126;	
			
			Flash_Write_Array_16bit(&flash_write_N[0],ris_temp, data+1);
			delay(100);
			Flash_Write_Array_16bit(&flash_write_T[0],ris_timer , data+1);
			delay(100);
			bufcl();
			lcd_clear();
			
			lcd_put_cur(0,0);
			
			
			lcd_send_string ("da luu"); 
		
			delay(50);
			_write =0;
		lcd_clear();		//	Flash_Read_Array_16bit(arr_Read_1,ris_1, data+1);

		
			lcd_clear(); 
			lcd_put_cur(0,0);
			lcd_send_string ("run: D");
			delay(100);
			check =2;
			return;
	
		}delay(10);
	}while(1);				//Flash_Write_Uint(data, 1)
		
}






void num_read_fl(){

//	num_key_timer()
	
	
			uint32_t	flash_length = 0x08000000 +1024*123;

			uint16_t num_arr_read = Flash_Read_Uint(	flash_length );
			lcd_clear();
			bufcl();
			sprintf(buf,"so da luu:%d",num_arr_read);
			lcd_send_string (buf);
		
	
		
		
			delay(20);
			uint16_t arr_flash_temp[num_arr_read] ;
			uint16_t arr_flash_timer[num_arr_read] ;
				
			uint32_t	ris_temp 	=	0x08000000 +1024*60;
			uint32_t	ris_timer =  0x08000000 +1024*62;	
		
			Flash_Read_Array_16bit(arr_flash_temp ,ris_temp, num_arr_read+1);
	
			Flash_Read_Array_16bit(arr_flash_timer ,ris_timer, num_arr_read +1);

	
			lcd_clear(); 
			lcd_put_cur(0,0);
			lcd_send_string ("da doc du lieu");
			HAL_Delay(40);
			lcd_clear();
uint8_t check_temp =10;
uint8_t check_timer =0;
uint8_t flash_start =0;
	while(1){
					uint8_t TEC = num_adc();
		millis();
lcd_put_cur(1,0);
		bufcl();
		sprintf(buf,"T:%d",millis());
		lcd_send_string (buf);
	if(millis() > 100*check_timer)
		{
		timer_t() ;
					check_temp  = arr_flash_temp[flash_start];
					check_timer = arr_flash_timer[flash_start];
		
		
					lcd_put_cur(0,0);
					bufcl();					sprintf(buf,"%d  |N:%d-T:%d|",flash_start ,check_temp,check_timer );
					lcd_send_string (buf);				
			flash_start++;
	}
	
		
				if(TEC	< check_temp)
				{
				
				//	HAL_GPIO_WritePin(GPIOB, GPIO_PIN_0,GPIO_PIN_SET);
				//	HAL_GPIO_WritePin(GPIOB, GPIO_PIN_1,GPIO_PIN_RESET);
					delay(5);

				}else if(TEC> check_temp +5){lcd_put_cur(0,0);
					
						
					//	HAL_GPIO_WritePin(GPIOB, GPIO_PIN_0,GPIO_PIN_RESET);
						//HAL_GPIO_WritePin(GPIOB, GPIO_PIN_1,GPIO_PIN_SET);	
						delay(5);
				}	else if(TEC>=check_temp&& TEC<(check_temp +5)){
					//	HAL_GPIO_WritePin(GPIOB, GPIO_PIN_0,GPIO_PIN_RESET);
					//	HAL_GPIO_WritePin(GPIOB, GPIO_PIN_1,GPIO_PIN_SET);	
						delay(1);
				}
					
			
				
	
						
		
					
					while(wait ==1);
				
				if(stop ==1)
					{
						return;
					}
					if(flash_start >= num_arr_read )
					{lcd_clear(); 
			lcd_put_cur(0,0);
			lcd_send_string ("xong");
					break;				
					}
			delay(1);	
					
					
	}

}




/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_DMA_Init(void);
static void MX_ADC1_Init(void);
static void MX_TIM2_Init(void);

	
	
	void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin) // interrup
{ 
  /* Prevent unused argument(s) compilation warning */
	

  UNUSED(GPIO_Pin);

  if(GPIO_Pin==GPIO_PIN_0){
		  start = !start;
	
  }
	if(GPIO_Pin==GPIO_PIN_1){
      check ++; 
	if( check>3){ check =0;};
  }
	
	if(GPIO_Pin==GPIO_PIN_2){
	start =0;
	stop = !stop;
	
  }
}

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{

  HAL_Init();

 
  SystemClock_Config();


  MX_GPIO_Init();
  MX_DMA_Init();
  MX_ADC1_Init();
  MX_TIM2_Init();
  MX_I2C1_Init();
  /* USER CODE BEGIN 2 */
lcd_init ();
  /* USER CODE END 2 */
 HAL_TIM_Base_Start(&htim2);
lcd_put_cur(1,6);
	
	lcd_send_string ("k:");
	/*
	lcd_put_cur(0,0);
	uint32_t	ris_temp 	=	0x08000000 +1024*124;
			uint32_t	ris_timer =  0x08000000 +1024*126;	
			
			uint16_t flash_write_N[3] ;
			uint16_t flash_write_T[3] ;
				flash_write_N[0] =1;
				flash_write_N[1] =2;
				flash_write_N[2] =3;
				flash_write_T[0] =4;
				flash_write_T[1] =5;
				flash_write_T[2] =6;
				
			Flash_Write_Array_16bit(&flash_write_N[0],ris_temp, 3);
			delay(100);	lcd_send_string ("1:");
			Flash_Write_Array_16bit(&flash_write_T[0],ris_timer ,3);
			delay(100);
		lcd_send_string ("2");
			uint16_t arr_flash_temp[3] ;
			uint16_t arr_flash_timer[3] ;
				
			
		
			Flash_Read_Array_16bit(arr_flash_temp ,ris_temp, 3);
		lcd_send_string ("3:");
			Flash_Read_Array_16bit(arr_flash_timer ,ris_timer, 3);
			for(uint8_t i=0; i<3; i++){
			bufcl();	lcd_put_cur(1,0);
				sprintf(buf,"%d ,N: %d, T:%d",i,arr_flash_temp[i],arr_flash_timer[i]);
					lcd_send_string (buf);
				delay(500);
			}
	delay(10000);
			
			*/
  while (1)
  {
		delay(2);
	uint8_t k_= Keypad_Read();	delay(2);
		/// 68 D read
															// 70 # write
	
		if(k_ != 0x01  ){bufcl();
		lcd_put_cur(1,6);
		sprintf(buf,"k:%d", k_ );
		lcd_send_string (buf);
		
		}
			
				if(k_ == 67)
					{

					num_write_flash();
					}else if(k_ == 68)
					{
				 num_read_fl(); // docj lai gia tri da luwu
					}
					delay(1);
		delay(10);
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
  RCC_PeriphCLKInitTypeDef PeriphClkInit = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_HSI;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
  {
    Error_Handler();
  }
  PeriphClkInit.PeriphClockSelection = RCC_PERIPHCLK_ADC;
  PeriphClkInit.AdcClockSelection = RCC_ADCPCLK2_DIV2;
  if (HAL_RCCEx_PeriphCLKConfig(&PeriphClkInit) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief ADC1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_ADC1_Init(void)
{

  /* USER CODE BEGIN ADC1_Init 0 */

  /* USER CODE END ADC1_Init 0 */

  ADC_ChannelConfTypeDef sConfig = {0};

  /* USER CODE BEGIN ADC1_Init 1 */

  /* USER CODE END ADC1_Init 1 */

  /** Common config
  */
  hadc1.Instance = ADC1;
  hadc1.Init.ScanConvMode = ADC_SCAN_DISABLE;
  hadc1.Init.ContinuousConvMode = DISABLE;
  hadc1.Init.DiscontinuousConvMode = DISABLE;
  hadc1.Init.ExternalTrigConv = ADC_SOFTWARE_START;
  hadc1.Init.DataAlign = ADC_DATAALIGN_RIGHT;
  hadc1.Init.NbrOfConversion = 1;
  if (HAL_ADC_Init(&hadc1) != HAL_OK)
  {
    Error_Handler();
  }

  /** Configure Regular Channel
  */
  sConfig.Channel = ADC_CHANNEL_3;
  sConfig.Rank = ADC_REGULAR_RANK_1;
  sConfig.SamplingTime = ADC_SAMPLETIME_1CYCLE_5;
  if (HAL_ADC_ConfigChannel(&hadc1, &sConfig) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN ADC1_Init 2 */

  /* USER CODE END ADC1_Init 2 */

}

/**
  * @brief I2C1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_I2C1_Init(void)
{

  /* USER CODE BEGIN I2C1_Init 0 */

  /* USER CODE END I2C1_Init 0 */

  /* USER CODE BEGIN I2C1_Init 1 */

  /* USER CODE END I2C1_Init 1 */
  hi2c1.Instance = I2C1;
  hi2c1.Init.ClockSpeed = 100000;
  hi2c1.Init.DutyCycle = I2C_DUTYCYCLE_2;
  hi2c1.Init.OwnAddress1 = 0;
  hi2c1.Init.AddressingMode = I2C_ADDRESSINGMODE_7BIT;
  hi2c1.Init.DualAddressMode = I2C_DUALADDRESS_DISABLE;
  hi2c1.Init.OwnAddress2 = 0;
  hi2c1.Init.GeneralCallMode = I2C_GENERALCALL_DISABLE;
  hi2c1.Init.NoStretchMode = I2C_NOSTRETCH_DISABLE;
  if (HAL_I2C_Init(&hi2c1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN I2C1_Init 2 */

  /* USER CODE END I2C1_Init 2 */

}

/**
  * @brief TIM2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM2_Init(void)
{

  /* USER CODE BEGIN TIM2_Init 0 */

  /* USER CODE END TIM2_Init 0 */

  TIM_ClockConfigTypeDef sClockSourceConfig = {0};
  TIM_MasterConfigTypeDef sMasterConfig = {0};

  /* USER CODE BEGIN TIM2_Init 1 */

  /* USER CODE END TIM2_Init 1 */
  htim2.Instance = TIM2;
  htim2.Init.Prescaler = 3999;
  htim2.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim2.Init.Period = 1999;
  htim2.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim2.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_Base_Init(&htim2) != HAL_OK)
  {
    Error_Handler();
  }
  sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
  if (HAL_TIM_ConfigClockSource(&htim2, &sClockSourceConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim2, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM2_Init 2 */

  /* USER CODE END TIM2_Init 2 */

}

/**
  * Enable DMA controller clock
  */

static void MX_DMA_Init(void)
{

  /* DMA controller clock enable */
  __HAL_RCC_DMA1_CLK_ENABLE();

  /* DMA interrupt init */
  /* DMA1_Channel1_IRQn interrupt configuration */
  HAL_NVIC_SetPriority(DMA1_Channel1_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(DMA1_Channel1_IRQn);

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
/* USER CODE BEGIN MX_GPIO_Init_1 */
/* USER CODE END MX_GPIO_Init_1 */

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOD_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_2, GPIO_PIN_SET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_12|GPIO_PIN_13|GPIO_PIN_14|GPIO_PIN_15, GPIO_PIN_RESET);

  /*Configure GPIO pins : PA0 PA1 PA2 */
  GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_2;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_FALLING;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pins : PB0 PB1 PB2 */
  GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_2;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pins : PB12 PB13 PB14 PB15 */
  GPIO_InitStruct.Pin = GPIO_PIN_12|GPIO_PIN_13|GPIO_PIN_14|GPIO_PIN_15;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_PULLDOWN;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pins : PA8 PA9 PA10 PA11 */
  GPIO_InitStruct.Pin = GPIO_PIN_8|GPIO_PIN_9|GPIO_PIN_10|GPIO_PIN_11;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /* EXTI interrupt init*/
  HAL_NVIC_SetPriority(EXTI1_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(EXTI1_IRQn);

  HAL_NVIC_SetPriority(EXTI2_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(EXTI2_IRQn);

/* USER CODE BEGIN MX_GPIO_Init_2 */
/* USER CODE END MX_GPIO_Init_2 */
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */

  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     tex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
