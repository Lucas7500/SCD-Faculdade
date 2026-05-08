import grpc
import temperature_pb2
import temperature_pb2_grpc
from const import GRPC_SERVER_ADDRESS

def run():
    with grpc.insecure_channel(GRPC_SERVER_ADDRESS) as channel:
        stub = temperature_pb2_grpc.TemperatureServiceStub(channel)
        
        print("--- Querying Latest Temperature ---")
        try:
            latest = stub.GetLatestTemperature(temperature_pb2.Empty())
            print(f"Latest: {latest.value}°C at {latest.timestamp} ({latest.type})")
        except grpc.RpcError as e:
            print(f"Error fetching latest: {e.code()}")

        print("\n--- Querying Historical Data ---")
        try:
            history = stub.GetHistoricalData(temperature_pb2.Empty())
            for reading in history.readings:
                print(f"{reading.timestamp}: {reading.value}°C ({reading.type})")
        except grpc.RpcError as e:
            print(f"Error fetching history: {e.code()}")

if __name__ == '__main__':
    run()
