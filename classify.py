import google.generativeai as genai

def classify_image_with_gemini(image_bytes: bytes, api_key: str) -> dict:
    genai.configure(api_key=api_key)

    prompt = """
    Berikut adalah gambar daun tanaman cabai. Tolong klasifikasikan kondisi daun tersebut ke dalam salah satu dari lima kategori berikut:

    1. Leaf Curl – daun terlihat keriting atau menggulung.
    2. Leaf Spot – daun memiliki bercak coklat/hitam tidak merata.
    3. Healthy – daun tampak hijau dan sehat tanpa gejala.
    4. Whitefly – terdapat tanda-tanda hama whitefly, seperti bintik putih atau kehadiran serangga.
    5. Yellowish – daun tampak kekuningan menyeluruh, bisa jadi karena kekurangan nutrisi atau penyakit.

    Berikan hasil klasifikasi dan alasanmu dalam format JSON dengan struktur sebagai berikut:

    {
      "klasifikasi": "Nama Kategori",
      "alasan": "Penjelasan alasan klasifikasi berdasarkan gambar"
    }

    Pastikan hanya mengembalikan JSON, tanpa penjelasan tambahan atau teks lainnya.
    """

    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content([
        prompt,
        {"mime_type": "image/jpeg", "data": image_bytes}
    ])

    import json
    import re

    try:
        # Hapus teks di luar blok JSON jika ada
        text = response.text.strip()

        # Ambil bagian JSON saja jika diawali dengan ```
        match = re.search(r'\{[\s\S]*\}', text)
        json_text = match.group(0) if match else text

        result = json.loads(json_text)
        return result
    except Exception as e:
        return {
            "klasifikasi": "Penyakit Tidak Dapat Diidentifikasi",
            "alasan": "Kualitas gambar kurang bagus atau gambar mungkin bukan gambar tanaman cabai",
            "raw_response": response.text
        }
