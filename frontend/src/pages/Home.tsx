import React, { useState, useEffect } from "react";
import { ItemForm } from "../components/ItemForm";
import { ItemList } from "../components/ItemList";
import { fetchItems } from "../utils/api";
import type { Item } from "../types/item";

export const Home: React.FC = () => {
  const [items, setItems] = useState<Item[]>([]);

  const loadItems = async () => {
    try {
      const data = await fetchItems();
      setItems(data);
    } catch (error) {
      console.error("Failed to load items", error);
    }
  };

  useEffect(() => {
    loadItems();
  }, []);

  return (
    <div className="flex flex-col items-center justify-start p-8 space-y-6">
      <h1 className="text-3xl font-bold mb-4 text-center">Item Management</h1>

      <ItemForm onSuccess={loadItems} />
      <ItemList items={items} />
    </div>
  );
};
