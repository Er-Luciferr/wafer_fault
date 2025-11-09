import sys , os
import numpy as np 
import pandas as pd 
from src.constant import *
from src.exception import CustomException
from src.logger import logging 
from src.utils import MainUtils 
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    artifact_folder: str = artifact_folder
    source_data_file: str = os.path.join(artifact_folder, 'wafer_fault.csv')

class DataIngestion:
    def __init__(self):

        self.data_ingestion_config = DataIngestionConfig()
        self.MainUtils = MainUtils()

    def read_data_from_file(self) -> pd.DataFrame:
        """
        Method Name :   read_data_from_file
        Description :   This method reads data from the source CSV file in artifacts folder. 
        
        Output      :   dataset is returned as a pd.DataFrame
        On Failure  :   Write an exception log and then raise an exception
        
        Version     :   1.0
       
        """
        try:
            logging.info(f"Reading data from file: {self.data_ingestion_config.source_data_file}")
            
            if not os.path.exists(self.data_ingestion_config.source_data_file):
                raise FileNotFoundError(
                    f"Source data file not found at: {self.data_ingestion_config.source_data_file}\n"
                    f"Please ensure the file 'wafer_fault.csv' exists in the artifacts folder."
                )
            
            df = pd.read_csv(self.data_ingestion_config.source_data_file)
            
            # Replace 'na' values with NaN
            df.replace({'na': np.nan}, inplace=True)
            
            logging.info(f"Successfully read {len(df)} rows from the source file")
            return df 

        except Exception as e:
            raise CustomException(e, sys) from e

    def export_data_into_feature_store_file_path(self) -> str:
        """
        Method Name :   export_data_into_feature_store
        Description :   This method reads data from CSV file and saves it into artifacts folder. 
        
        Output      :   feature store file path is returned
        On Failure  :   Write an exception log and then raise an exception
        
        Version     :   1.0
       
        """
        try:
            logging.info(f"Reading data from source file")
            raw_file_path = self.data_ingestion_config.artifact_folder
            os.makedirs(raw_file_path , exist_ok=True)

            # Read data from source file
            sensor_data = self.read_data_from_file()
            
            logging.info(f"Saving data into feature store file path: {raw_file_path}")

            feature_store_file_path = os.path.join(raw_file_path , 'wafer_fault.csv')
            sensor_data.to_csv(feature_store_file_path, index=False)

            logging.info(f"Data saved to feature store: {feature_store_file_path}")
            return feature_store_file_path

        except Exception as e:
            raise CustomException(e , sys) from e 

    def initiate_data_ingetion(self) -> str:
        """
            Method Name :   initiate_data_ingestion
            Description :   This method initiates the data ingestion components of training pipeline 
            
            Output      :   feature store file path is returned
            On Failure  :   Write an exception log and then raise an exception
            
            Version     :   1.0
            
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")

        try:
            feature_store_file_path = self.export_data_into_feature_store_file_path()

            logging.info('Got data from source file')

            logging.info(
                "Exited initiate_data_ingestion method of Data_Ingestion class"
            )
            return feature_store_file_path

        except Exception as e:
            raise CustomException(e,sys) from e 
