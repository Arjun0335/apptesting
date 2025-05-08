import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

export default function LoveWebsite() {
  return (
    <main className="min-h-screen bg-gradient-to-r from-pink-200 to-pink-400 flex items-center justify-center p-4">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1 }}
        className="w-full max-w-md"
      >
        <Card className="rounded-2xl shadow-xl p-6 bg-white">
          <CardContent className="space-y-6">
            <h1 className="text-3xl font-bold text-center text-pink-600">
              To the Love of My Life ❤️
            </h1>
            <p className="text-center text-gray-700">
              Every moment with you is a beautiful memory, and this small website is a token of my love for you.
            </p>

            <img
              src="couple.jpeg"
              alt="You my love"
              className="w-full h-64 object-cover rounded-xl shadow-md"
            />

            <ul className="text-center text-gray-800 list-disc list-inside space-y-1">
              <li>You light up my world like no one else 💫</li>
              <li>Your smile is my favorite view 😊</li>
              <li>Every day with you is a gift 🎁</li>
              <li>I’m lucky to have you by my side 🌹</li>
              <li>You are my forever and always 💖</li>
            </ul>

            <div className="text-center space-x-2">
              <Button className="bg-pink-500 hover:bg-pink-600 text-white px-6 py-2 rounded-full">
                I Love You ❤️
              </Button>
              <Button variant="outline" className="border-pink-400 text-pink-600 px-6 py-2 rounded-full">
                Send a Hug 🤗
              </Button>
            </div>
          </CardContent>
        </Card>
      </motion.div>
    </main>
  );
}
