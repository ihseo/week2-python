import requests

def main():
    response = requests.get("https://outback.60736ldvbpamu.ap-northeast-2.cs.amazonlightsail.com/participation/statistics")
    # print(response)
    print(response)
    # print(response.status_code)
    # print(response.headers['Content-Type'])  # html/css 
    # print("Content:", response.text)
    # GET POST PATCH PUT DELETE

if __name__ == "__main__":
    main()



