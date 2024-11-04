import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directory']
    
    # Proceso
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=f'{nombre_directorio}/')
    
    return {
        'statusCode': 200,
        'message': f'Directorio "{nombre_directorio}" creado en el bucket "{nombre_bucket}"'
    }
