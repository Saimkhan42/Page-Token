import requests

def get_page_access_tokens(user_access_token):
    # API URL to get the pages linked to the user
    url = f'https://graph.facebook.com/me/accounts?access_token={user_access_token}'

    # Send request to the Facebook API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        # Check if 'data' contains page info
        if 'data' in data:
            pages = data['data']
            if len(pages) == 0:
                print("No pages found for this user.")
            for page in pages:
                page_name = page.get('name')
                page_id = page.get('id')
                page_access_token = page.get('access_token')
                
                if page_access_token:
                    print(f"Page Name: {page_name}")
                    print(f"Page ID: {page_id}")
                    print(f"Access Token: {page_access_token}")
                    print("-" * 50)  # Separate different pages
                else:
                    print(f"Access Token not available for Page: {page_name}")
                    print("-" * 50)
        else:
            print("No pages found for this user.")
    else:
        print(f"Error: {response.json()}")

# User provides the access token as input
user_access_token = input("Enter your User Access Token: ")

# Call the function with the provided token
get_page_access_tokens(user_access_token)
