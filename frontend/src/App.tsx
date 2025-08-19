// frontend/src/App.tsx
import { useEffect, useState } from "react";

const API_BASE = import.meta.env.VITE_API_BASE_URL;

type Item = {
  id: number;
  name: string;
  description: string;
};

function App() {
  const [items, setItems] = useState<Item[]>([]);
  const [newItem, setNewItem] = useState({ name: "", description: "" });

  const fetchItems = async () => {
    const res = await fetch(`${API_BASE}/items`);
    const data = await res.json();
    setItems(data);
  };

  const addItem = async () => {
    const res = await fetch(`${API_BASE}/items`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newItem),
    });
    const created = await res.json();
    setItems([...items, created]);
    setNewItem({ name: "", description: "" });
  };

  useEffect(() => {
    fetchItems();
  }, []);

  return (
    <div style={{ padding: "1rem" }}>
      <h1>Items</h1>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            <b>{item.name}</b>: {item.description}
          </li>
        ))}
      </ul>
      <h2>Add Item</h2>
      <input
        placeholder="Name"
        value={newItem.name}
        onChange={(e) => setNewItem({ ...newItem, name: e.target.value })}
      />
      <input
        placeholder="Description"
        value={newItem.description}
        onChange={(e) =>
          setNewItem({ ...newItem, description: e.target.value })
        }
      />
      <button onClick={addItem}>Add</button>
    </div>
  );
}

export default App;
