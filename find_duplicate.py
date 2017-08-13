# Note that summing up the numbers or XOR of the numbers is not going to work in this case.
#
# Can you try solving the problem in sqrt(n) space?
#
# Split the numbers from 1 to n in sqrt(n) ranges so that range i corresponds to [sqrt(n) * i .. sqrt(n) * (i + 1)).

import math


def find_duplicate(vs):
    input_length = len(vs)
    if input_length == 0:
        return -1
    n = input_length - 1
    n_ranges = math.floor(math.sqrt(n))
    max_range_size = math.ceil(n / n_ranges)
    assert n_ranges <= max_range_size
    buckets = [0] * max_range_size

    def range_index(value):
        return (value - 1) // max_range_size

    for v in vs:
        buckets[range_index(v)] += 1

    def select_overfilled_bucket(bs, max_bucket_size):
        for i, b in enumerate(bs):
            if b > max_bucket_size:
                return i
        return n_ranges - 1

    overfilled_range_index = select_overfilled_bucket(buckets, max_range_size)
    overfilled_range_min = overfilled_range_index * max_range_size + 1

    for i in range(max_range_size):
        buckets[i] = 0

    for v in vs:
        if range_index(v) == overfilled_range_index:
            buckets[v - overfilled_range_min] += 1

    for i, b in enumerate(buckets):
        if b > 1:
            return i + overfilled_range_min

    return -1  # should never happen


# assert find_duplicate([3, 4, 1, 4, 1]) == 4
# assert find_duplicate([3, 1, 4, 1, 1]) == 1
# assert find_duplicate([3, 1, 2, 1]) == 1
# assert find_duplicate([ 247, 240, 303, 9, 304, 105, 44, 204, 291, 26, 242, 2, 358, 264, 176, 289, 196, 329, 189, 102, 45, 111, 115, 339, 74, 200, 34, 201, 215, 173, 107, 141, 71, 125, 6, 241, 275, 88, 91, 58, 171, 346, 219, 238, 246, 10, 118, 163, 287, 179, 123, 348, 283, 313, 226, 324, 203, 323, 28, 251, 69, 311, 330, 316, 320, 312, 50, 157, 342, 12, 253, 180, 112, 90, 16, 288, 213, 273, 57, 243, 42, 168, 55, 144, 131, 38, 317, 194, 355, 254, 202, 351, 62, 80, 134, 321, 31, 127, 232, 67, 22, 124, 271, 231, 162, 172, 52, 228, 87, 174, 307, 36, 148, 302, 198, 24, 338, 276, 327, 150, 110, 188, 309, 354, 190, 265, 3, 108, 218, 164, 145, 285, 99, 60, 286, 103, 119, 29, 75, 212, 290, 301, 151, 17, 147, 94, 138, 272, 279, 222, 315, 116, 262, 1, 334, 41, 54, 208, 139, 332, 89, 18, 233, 268, 7, 214, 20, 46, 326, 298, 101, 47, 236, 216, 359, 161, 350, 5, 49, 122, 345, 269, 73, 76, 221, 280, 322, 149, 318, 135, 234, 82, 120, 335, 98, 274, 182, 129, 106, 248, 64, 121, 258, 113, 349, 167, 192, 356, 51, 166, 77, 297, 39, 305, 260, 14, 63, 165, 85, 224, 19, 27, 177, 344, 33, 259, 292, 100, 43, 314, 170, 97, 4, 78, 310, 61, 328, 199, 255, 159, 185, 261, 229, 11, 295, 353, 186, 325, 79, 142, 223, 211, 152, 266, 48, 347, 21, 169, 65, 140, 83, 156, 340, 56, 220, 130, 117, 143, 277, 235, 59, 205, 153, 352, 300, 114, 84, 183, 333, 230, 197, 336, 244, 195, 37, 23, 206, 86, 15, 187, 181, 308, 109, 293, 128, 66, 270, 209, 158, 32, 25, 227, 191, 35, 40, 13, 175, 146, 299, 207, 217, 281, 30, 357, 184, 133, 245, 284, 343, 53, 210, 306, 136, 132, 239, 155, 73, 193, 278, 257, 126, 331, 294, 250, 252, 263, 92, 267, 282, 72, 95, 337, 154, 319, 341, 70, 81, 68, 160, 8, 249, 96, 104, 137, 256, 93, 178, 296, 225, 237 ]) == 73
# assert find_duplicate([ 310, 164, 385, 493, 296, 369, 405, 421, 24, 187, 98, 109, 245, 324, 464, 438, 467, 526, 19, 39, 206, 128, 380, 119, 129, 85, 131, 510, 132, 40, 332, 275, 51, 528, 412, 525, 4, 259, 356, 258, 90, 66, 153, 223, 414, 89, 410, 227, 291, 314, 358, 204, 340, 436, 7, 188, 325, 538, 182, 141, 408, 198, 42, 337, 214, 509, 349, 79, 116, 428, 53, 91, 326, 333, 33, 415, 165, 271, 183, 244, 330, 392, 123, 522, 437, 420, 362, 331, 286, 84, 130, 163, 145, 483, 190, 482, 115, 16, 496, 418, 267, 240, 175, 65, 276, 154, 173, 355, 315, 504, 101, 260, 458, 274, 413, 497, 15, 213, 398, 473, 284, 456, 397, 309, 344, 5, 402, 229, 347, 236, 254, 140, 472, 391, 336, 535, 533, 25, 429, 475, 441, 352, 434, 26, 45, 75, 257, 57, 46, 442, 536, 209, 411, 146, 432, 34, 118, 346, 23, 512, 71, 480, 107, 321, 126, 52, 407, 393, 515, 217, 195, 294, 86, 502, 72, 517, 455, 281, 495, 230, 108, 295, 424, 426, 460, 524, 452, 181, 185, 208, 180, 47, 303, 520, 36, 200, 530, 12, 67, 445, 492, 419, 372, 105, 59, 306, 317, 379, 150, 63, 363, 248, 505, 167, 152, 404, 516, 316, 433, 70, 439, 390, 9, 133, 298, 232, 95, 157, 176, 215, 172, 224, 169, 127, 106, 8, 537, 135, 255, 313, 375, 241, 506, 253, 312, 11, 448, 139, 263, 2, 112, 21, 304, 297, 334, 278, 162, 142, 343, 328, 280, 69, 311, 486, 457, 285, 219, 499, 226, 329, 521, 374, 489, 76, 231, 193, 447, 431, 148, 444, 371, 256, 211, 365, 339, 56, 459, 350, 58, 269, 242, 249, 30, 43, 113, 177, 476, 364, 465, 3, 96, 484, 99, 147, 501, 270, 425, 49, 487, 55, 373, 377, 400, 422, 477, 282, 423, 272, 384, 399, 498, 323, 238, 144, 83, 44, 327, 158, 386, 287, 409, 216, 196, 277, 307, 235, 401, 466, 32, 22, 299, 471, 81, 378, 265, 137, 288, 159, 283, 268, 395, 387, 13, 292, 490, 6, 122, 417, 243, 239, 203, 31, 293, 82, 485, 381, 202, 197, 273, 403, 446, 383, 77, 60, 435, 102, 361, 205, 481, 353, 474, 301, 94, 125, 184, 367, 20, 151, 222, 237, 17, 290, 523, 468, 156, 266, 149, 443, 289, 394, 513, 28, 519, 191, 507, 518, 478, 251, 396, 532, 416, 440, 247, 35, 234, 308, 37, 302, 341, 1, 121, 138, 279, 469, 10, 233, 74, 61, 124, 78, 220, 194, 494, 252, 88, 110, 189, 18, 261, 48, 38, 41, 114, 318, 479, 406, 360, 97, 454, 68, 136, 503, 451, 100, 178, 160, 186, 514, 322, 210, 73, 212, 103, 54, 354, 500, 225, 450, 335, 305, 170, 462, 228, 348, 199, 262, 143, 111, 155, 92, 319, 345, 491, 192, 14, 166, 207, 171, 338, 168, 250, 27, 389, 368, 117, 351, 201, 179, 221, 529, 93, 87, 104, 134, 357, 359, 50, 430, 531, 488, 470, 449, 342, 320, 134, 64, 62, 246, 511, 527, 388, 453, 264, 463, 370, 120, 508, 376, 461, 174, 382, 427, 161, 80, 29, 300, 366, 218, 534 ]) == 134
# assert find_duplicate([ 442, 249, 406, 112, 202, 98, 228, 99, 38, 10, 402, 505, 104, 340, 265, 317, 190, 403, 148, 276, 145, 199, 456, 489, 237, 226, 470, 342, 405, 339, 142, 234, 542, 96, 71, 297, 261, 262, 130, 119, 428, 82, 432, 219, 430, 439, 188, 397, 227, 478, 400, 111, 451, 388, 34, 303, 158, 68, 74, 502, 36, 80, 243, 508, 73, 324, 103, 325, 46, 211, 133, 144, 480, 404, 231, 416, 401, 370, 3, 48, 407, 195, 212, 300, 47, 409, 44, 21, 248, 105, 56, 319, 117, 149, 334, 455, 544, 429, 464, 143, 75, 197, 316, 292, 352, 282, 525, 194, 87, 242, 283, 333, 356, 440, 338, 100, 366, 368, 520, 129, 479, 499, 408, 496, 307, 173, 347, 101, 293, 523, 114, 5, 393, 178, 329, 394, 302, 59, 492, 175, 537, 538, 454, 217, 84, 344, 126, 360, 471, 433, 238, 465, 62, 165, 43, 139, 530, 512, 280, 312, 518, 385, 8, 29, 93, 467, 320, 64, 120, 452, 391, 358, 522, 445, 274, 240, 172, 449, 205, 18, 328, 453, 278, 536, 69, 331, 166, 92, 50, 462, 501, 27, 106, 72, 30, 11, 289, 318, 343, 245, 497, 411, 218, 363, 151, 85, 37, 337, 285, 511, 137, 426, 155, 254, 376, 136, 235, 90, 418, 60, 487, 181, 232, 486, 287, 515, 362, 86, 395, 255, 159, 527, 336, 378, 375, 115, 15, 179, 33, 67, 177, 247, 51, 424, 284, 357, 157, 162, 253, 135, 216, 122, 41, 118, 359, 209, 355, 373, 437, 23, 214, 97, 191, 447, 83, 267, 256, 20, 52, 236, 39, 259, 204, 353, 510, 55, 203, 305, 290, 206, 413, 488, 14, 380, 174, 540, 299, 463, 485, 371, 309, 186, 481, 192, 200, 156, 288, 534, 475, 382, 184, 152, 220, 189, 521, 443, 110, 160, 369, 171, 183, 468, 65, 108, 427, 423, 516, 146, 384, 138, 222, 35, 365, 163, 458, 132, 498, 372, 66, 345, 326, 396, 40, 141, 22, 491, 19, 286, 415, 434, 121, 1, 270, 313, 78, 446, 379, 392, 31, 9, 180, 420, 45, 76, 26, 460, 49, 89, 279, 54, 57, 208, 519, 241, 275, 386, 441, 533, 296, 507, 422, 109, 196, 361, 2, 4, 474, 182, 53, 310, 414, 291, 364, 61, 535, 398, 134, 24, 509, 335, 484, 263, 476, 154, 304, 25, 306, 444, 32, 266, 210, 539, 473, 322, 7, 466, 529, 436, 350, 494, 16, 161, 116, 459, 168, 301, 215, 213, 91, 438, 102, 224, 277, 13, 17, 28, 258, 70, 531, 541, 532, 315, 187, 381, 170, 272, 147, 223, 252, 421, 81, 271, 201, 164, 176, 58, 257, 321, 95, 377, 472, 113, 94, 457, 153, 469, 225, 140, 399, 281, 308, 230, 193, 390, 514, 483, 412, 327, 12, 543, 367, 493, 504, 419, 524, 198, 77, 295, 417, 389, 374, 435, 42, 330, 528, 311, 490, 387, 341, 517, 127, 298, 169, 185, 125, 233, 410, 477, 128, 239, 107, 448, 354, 221, 425, 264, 294, 323, 88, 526, 124, 351, 349, 506, 150, 348, 246, 482, 260, 251, 167, 503, 250, 268, 273, 207, 540, 332, 63, 431, 131, 383, 6, 495, 244, 346, 269, 79, 450, 513, 123, 461, 314, 229, 500 ]) == 540
print(find_duplicate([ 442, 249, 406, 112, 202, 98, 228, 99, 38, 10, 402, 505, 104, 340, 265, 317, 190, 403, 148, 276, 145, 199, 456, 489, 237, 226, 470, 342, 405, 339, 142, 234, 542, 96, 71, 297, 261, 262, 130, 119, 428, 82, 432, 219, 430, 439, 188, 397, 227, 478, 400, 111, 451, 388, 34, 303, 158, 68, 74, 502, 36, 80, 243, 508, 73, 324, 103, 325, 46, 211, 133, 144, 480, 404, 231, 416, 401, 370, 3, 48, 407, 195, 212, 300, 47, 409, 44, 21, 248, 105, 56, 319, 117, 149, 334, 455, 544, 429, 464, 143, 75, 197, 316, 292, 352, 282, 525, 194, 87, 242, 283, 333, 356, 440, 338, 100, 366, 368, 520, 129, 479, 499, 408, 496, 307, 173, 347, 101, 293, 523, 114, 5, 393, 178, 329, 394, 302, 59, 492, 175, 537, 538, 454, 217, 84, 344, 126, 360, 471, 433, 238, 465, 62, 165, 43, 139, 530, 512, 280, 312, 518, 385, 8, 29, 93, 467, 320, 64, 120, 452, 391, 358, 522, 445, 274, 240, 172, 449, 205, 18, 328, 453, 278, 536, 69, 331, 166, 92, 50, 462, 501, 27, 106, 72, 30, 11, 289, 318, 343, 245, 497, 411, 218, 363, 151, 85, 37, 337, 285, 511, 137, 426, 155, 254, 376, 136, 235, 90, 418, 60, 487, 181, 232, 486, 287, 515, 362, 86, 395, 255, 159, 527, 336, 378, 375, 115, 15, 179, 33, 67, 177, 247, 51, 424, 284, 357, 157, 162, 253, 135, 216, 122, 41, 118, 359, 209, 355, 373, 437, 23, 214, 97, 191, 447, 83, 267, 256, 20, 52, 236, 39, 259, 204, 353, 510, 55, 203, 305, 290, 206, 413, 488, 14, 380, 174, 540, 299, 463, 485, 371, 309, 186, 481, 192, 200, 156, 288, 534, 475, 382, 184, 152, 220, 189, 521, 443, 110, 160, 369, 171, 183, 468, 65, 108, 427, 423, 516, 146, 384, 138, 222, 35, 365, 163, 458, 132, 498, 372, 66, 345, 326, 396, 40, 141, 22, 491, 19, 286, 415, 434, 121, 1, 270, 313, 78, 446, 379, 392, 31, 9, 180, 420, 45, 76, 26, 460, 49, 89, 279, 54, 57, 208, 519, 241, 275, 386, 441, 533, 296, 507, 422, 109, 196, 361, 2, 4, 474, 182, 53, 310, 414, 291, 364, 61, 535, 398, 134, 24, 509, 335, 484, 263, 476, 154, 304, 25, 306, 444, 32, 266, 210, 539, 473, 322, 7, 466, 529, 436, 350, 494, 16, 161, 116, 459, 168, 301, 215, 213, 91, 438, 102, 224, 277, 13, 17, 28, 258, 70, 531, 541, 532, 315, 187, 381, 170, 272, 147, 223, 252, 421, 81, 271, 201, 164, 176, 58, 257, 321, 95, 377, 472, 113, 94, 457, 153, 469, 225, 140, 399, 281, 308, 230, 193, 390, 514, 483, 412, 327, 12, 543, 367, 493, 504, 419, 524, 198, 77, 295, 417, 389, 374, 435, 42, 330, 528, 311, 490, 387, 341, 517, 127, 298, 169, 185, 125, 233, 410, 477, 128, 239, 107, 448, 354, 221, 425, 264, 294, 323, 88, 526, 124, 351, 349, 506, 150, 348, 246, 482, 260, 251, 167, 503, 250, 268, 273, 207, 540, 332, 63, 431, 131, 383, 6, 495, 244, 346, 269, 79, 450, 513, 123, 461, 314, 229, 500 ]))

