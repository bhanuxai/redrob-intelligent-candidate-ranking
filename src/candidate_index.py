import pickle

from preprocess import (
    load_candidates,
    clean_candidate,
    DATA_FILE
)

from feature_builder import build_features

OUTPUT_FILE = "data/candidate_index.pkl"

def build_candidate_index():
    candidate_index = {}
    for i, candidate in enumerate(load_candidates(DATA_FILE), start=1):
        candidate = clean_candidate(candidate)
        features = build_features(candidate)
        candidate_id = candidate["candidate_id"]
        candidate_index[candidate_id] = features
        if i % 5000 == 0:
            print(f"Processed {i} candidates...")
    return candidate_index

def save_candidate_index(candidate_index, output_file):
    with open(output_file, "wb") as f:
        pickle.dump(candidate_index, f)
    print(f"Candidate index saved to {output_file}")

if __name__ == "__main__":
    index = build_candidate_index()
    save_candidate_index(index, OUTPUT_FILE)
    print(f"Total Candidates: {len(index)}")