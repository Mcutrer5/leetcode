public class Solution {
    public string MostCommonWord(string paragraph, string[] banned) {
        var words = paragraph.Split(new char[] {' ', ',', ';', '.', '!', '?', '\'', '\"', '(', ')', '[', ']', '{', '}', '\t', '\r', '\n'}, StringSplitOptions.RemoveEmptyEntries);
        var dict = new Dictionary<string, int>();
        foreach (var word in words)
        {
            var w = word.ToLower();
            if (dict.ContainsKey(w))
            {
                dict[w]++;
            }
            else
            {
                dict.Add(w, 1);
            }
        }
        var max = 0;
        var result = "";
        foreach (var kvp in dict)
        {
            if (kvp.Value > max && !banned.Contains(kvp.Key))
            {
                max = kvp.Value;
                result = kvp.Key;
            }
        }
        return result;
    }
}