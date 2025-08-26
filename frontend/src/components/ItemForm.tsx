import React, { useState } from "react";
import { createItem } from "../utils/api";
import { Button } from "./Button";

type ItemFormProps = {
  onSuccess?: () => void;
};

export const ItemForm: React.FC<ItemFormProps> = ({ onSuccess }) => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  const handleSubmit = async () => {
    if (!name) return alert("Name is required");

    try {
      await createItem({ name, description });
      setName("");
      setDescription("");
      setSuccessMessage("Added successfully.");
      if (onSuccess) onSuccess();

      setTimeout(() => setSuccessMessage(""), 3000);
    } catch (error) {
      setSuccessMessage("Failed to add, please try again later.");
    }
  };

  return (
    <div className="mb-4">
      <h2 className="text-xl font-bold mb-2">Add New Item</h2>
      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        className="border px-2 py-1 mr-2"
      />
      <input
        type="text"
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        className="border px-2 py-1 mr-2"
      />
      <Button onClick={handleSubmit}>
      Add Item
      </Button>
      {successMessage && (
        <span className="text-green-600 font-medium">{successMessage}</span>
      )}
    </div>
  );
};
