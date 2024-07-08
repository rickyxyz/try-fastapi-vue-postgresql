import axios from "../axios";

export const submitRating = async (rating) => {
  try {
    const response = await axios.post("/reviews/", { rating });
    return response.data;
  } catch (error) {
    console.error("Error submitting rating:", error);
    throw new Error("Failed to submit rating");
  }
};

export const fetchReviews = async () => {
  try {
    const response = await axios.get("/reviews/");
    return response.data;
  } catch (error) {
    console.error("Error fetching reviews:", error);
    throw new Error("Failed to fetch reviews");
  }
};
