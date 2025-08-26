import type { Item } from "../types/item";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const fetchItems = async (): Promise<Item[]> => {
  const res = await fetch(`${API_BASE_URL}/items`);
  if (!res.ok) throw new Error("Failed to fetch items");
  return res.json();
};

export const createItem = async (item: Omit<Item, "id">): Promise<Item> => {
  const res = await fetch(`${API_BASE_URL}/items`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item),
  });
  if (!res.ok) throw new Error("Failed to create item");
  return res.json();
};
