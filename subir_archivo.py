import boto3
import base64

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directory']
    nombre_archivo = event['body']['filename']
    contenido_archivo = base64.b64decode(event['body']['fileContent'])
    
    # Proceso
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=f'{nombre_directorio}/{nombre_archivo}', Body=contenido_archivo)
    
    return {
        'statusCode': 200,
        'message': f'Archivo "{nombre_archivo}" subido exitosamente en el directorio "{nombre_directorio}" del bucket "{nombre_bucket}"'
    }
