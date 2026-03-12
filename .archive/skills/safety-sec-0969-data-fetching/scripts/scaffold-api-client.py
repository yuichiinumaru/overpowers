#!/usr/bin/env python3
import os
import sys

def main():
    print("Scaffolding API Client based on Expo Networking patterns...")
    
    api_dir = "api"
    if not os.path.exists(api_dir):
        os.makedirs(api_dir)
        print(f"Created directory: {api_dir}")

    client_content = """import * as SecureStore from "expo-secure-store";

const BASE_URL = process.env.EXPO_PUBLIC_API_URL;
const TOKEN_KEY = "auth_token";

if (!BASE_URL) {
  throw new Error("EXPO_PUBLIC_API_URL is not defined");
}

export const auth = {
  getToken: () => SecureStore.getItemAsync(TOKEN_KEY),
  setToken: (token: string) => SecureStore.setItemAsync(TOKEN_KEY, token),
  removeToken: () => SecureStore.deleteItemAsync(TOKEN_KEY),
};

export class ApiError extends Error {
  constructor(message: string, public status: number, public code?: string) {
    super(message);
    this.name = "ApiError";
  }
}

export const apiClient = {
  get: async <T>(path: string): Promise<T> => {
    const token = await auth.getToken();
    const response = await fetch(`${BASE_URL}${path}`, {
      headers: {
        Authorization: token ? `Bearer ${token}` : "",
      },
    });
    
    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new ApiError(error.message || "Request failed", response.status, error.code);
    }
    return response.json();
  },

  post: async <T>(path: string, body: unknown): Promise<T> => {
    const token = await auth.getToken();
    const response = await fetch(`${BASE_URL}${path}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: token ? `Bearer ${token}` : "",
      },
      body: JSON.stringify(body),
    });
    
    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new ApiError(error.message || "Request failed", response.status, error.code);
    }
    return response.json();
  },
};
"""

    with open(os.path.join(api_dir, "client.ts"), "w") as f:
        f.write(client_content)
    print(f"Created: {os.path.join(api_dir, 'client.ts')}")

if __name__ == "__main__":
    main()
