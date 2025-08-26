import React from "react";
import type { Item } from "../types/item";

type ItemListProps = {
  items: Item[];
};

export const ItemList: React.FC<ItemListProps> = ({ items }) => {
  if (!items.length) return <p>No items found.</p>;

  return (
    <div className="w-full max-w-4xl mx-auto">
      <table className="border-collapse border border-gray-400 w-full">
        <thead>
          <tr>
            <th className="border border-gray-300 px-2 py-1 text-center">ID</th>
            <th className="border border-gray-300 px-2 py-1 text-center">
              Name
            </th>
            <th className="border border-gray-300 px-2 py-1 text-center">
              Description
            </th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr key={item.id}>
              <td className="border border-gray-300 px-2 py-1 text-center">
                {item.id}
              </td>
              <td className="border border-gray-300 px-2 py-1 text-center">
                {item.name}
              </td>
              <td className="border border-gray-300 px-2 py-1 text-center">
                {item.description}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
